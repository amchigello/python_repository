from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("spark_work").setMaster("local")
sc = SparkContext(conf=conf)


num = range(1, 20)
rdd1 = sc.parallelize(num)

print("Number of partitions: {}".format(rdd.getNumPartitions()))
print("Partitioner: {}".format(rdd.partitioner))
print("Partitions structure: {}".format(rdd.glom().collect()))
