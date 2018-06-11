# encoding: utf8

import click
import oss2


@click.command()
@click.option('access_key_id', '--access-key-id')
@click.option('access_key_secret', '--access-key-secret')
@click.option('endpoint', '--endpoint', default='oss-cn-hangzhou.aliyuncs.com')
@click.option('bucket_name', '--bucket-name')
def oss_delete_bucket(access_key_id, access_key_secret, endpoint, bucket_name):
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    while True:
        list_object_result = bucket.list_objects(max_keys=1000)
        if not list_object_result.object_list:
            break

        for obj in list_object_result.object_list:
            bucket.delete_object(obj.key)
            print 'delete object %s' % obj.key

    bucket.delete_bucket()
    print 'delete bucket %s successfully' % bucket_name


if __name__ == '__main__':
    oss_delete_bucket()

