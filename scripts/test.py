# Databricks notebook source
from datetime import datetime, timedelta
from pyspark.sql.functions import lit, col, when, current_date, to_date
from pyspark.sql.window import Window
import pyspark.sql.functions as func
from pyspark.sql.types import IntegerType, DecimalType
import json

incrementbyOne = Window.orderBy(lit("col"))
spark.conf.set("fs.azure.account.key.80013adlsgen2.blob.core.windows.net",
               "cB5QsbxOjzzhlklH0XHPRc4mk13+FwUeIGqHrNlEl7Muixho7om8I5JSepVDVtOHtPPG8RB/aehfPf7FJwXtwA==")


#################

instaplanheader_df = spark.read \
    .option("header", "true")\
    .option("inferSchema", "true")\
    .csv('wasbs://staging@80013adlsgen2.blob.core.windows.net/instaplanheader.csv')

debt_trans_df = spark.read \
    .option("header", "true")\
    .option("inferSchema", "true")\
    .csv("wasbs://staging@80013adlsgen2.blob.core.windows.net/debt_trans.csv")


instaplanheader_df = instaplanheader_df.withColumn("CREATION_DATE", instaplanheader_df.CREATION_DATE.cast("date"))\
    .withColumn("IN_PROGRESS_END_DT", instaplanheader_df.IN_PROGRESS_END_DT.cast("date"))

debt_trans_df = debt_trans_df.withColumn(
    "ACT_PAYMENT_DATE", debt_trans_df.ACT_PAYMENT_DATE.cast("date"))

instaplanheader_df.show()

# debt_trans_df.show()

# get the first of the month
debt_trans_trunc_df = debt_trans_df.withColumn(
    "first_of_payment_month", func.trunc(debt_trans_df.ACT_PAYMENT_DATE, 'month'))
debt_trans_trunc_df.show()

#################


#################

# get only the relevent instaplan header, by filtering the non essential accounts
debt_trans_filtered_df = debt_trans_trunc_df.select("DEBT_CODE").distinct()
instaplanheader_df_filtered = instaplanheader_df.alias('a').join(debt_trans_filtered_df, instaplanheader_df.DEBT_CODE ==
                                                                 debt_trans_filtered_df.DEBT_CODE, how='inner').select([col("a."+cols) for cols in instaplanheader_df.columns])

#################

# Mark all the payments with first_of_payment_month not falling between CREATION_DATE and IN_PROGRESS_END_DT as FLAG_NEW_BUSINESS
plans_recordset = instaplanheader_df_filtered.alias("plans")
payments_recordset = debt_trans_trunc_df.alias("payments")
range_payment_df = payments_recordset.join(plans_recordset, (payments_recordset.DEBT_CODE == plans_recordset.DEBT_CODE) &
                                           (payments_recordset.first_of_payment_month.between(plans_recordset.CREATION_DATE,
                                                                                              func.coalesce(
                                                                                                  plans_recordset.IN_PROGRESS_END_DT, current_date())
                                                                                              )), how='left')\
    .select([col("payments."+cols) for cols in payments_recordset.columns]+[col('plans.CREATION_DATE')])
flag_new_business_df = range_payment_df.select('DEBT_CODE', 'ACT_PAYMENT_DATE', func.when(
    range_payment_df['CREATION_DATE'].isNull(), 1).otherwise(0).alias("FLAG_NEW_BUSINESS"))

# .withColumn("flag_new_business",func.when(range_payment_df['CREATION_DATE'].isNull(),1).otherwise(0))

#################

flag_new_business_df.show()
