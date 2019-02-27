import boto3
 
def rename_s3_files_from_folder(bucket_name, src_folder, tgt_folder, rename_pattern):
    """
    :bucket_name: s3 bucket name of the file
    :src_folder: s3 directory where the original files are present
    :tgt_folder: s3 directory where the renamed files have to b e moved
    :rename_pattern: replace keyword part by this parameter
 
    Function copies the the files from one s3 directory to another,
    renaming them in the process and after copying deletes the file
    from the original directory
 
    """
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        for objects in bucket.objects.filter(Prefix=src_folder):
            file_keys = objects.key
            if not file_keys.endswith('/'):
                file_name = file_keys.split('/')[-1]
                dest_file_key = tgt_folder + '/' + \
                    file_name.replace('part', rename_pattern)
                copy_source = bucket_name + '/' + file_keys
                s3.Object(bucket_name, dest_file_key).copy_from(
                    CopySource=copy_source)
                print('copying {} from {} to {} successful'.format(
                    file_name, copy_source, dest_file_key))
            s3.Object(bucket_name, file_keys).delete()  # Delete Original File
            print('Deleting {} '.format(file_keys))
    except Exception as err:
        print(err)
        print('copying {} from {} to {} FAILED!'.format(
            file_name, copy_source, dest_file_key))
