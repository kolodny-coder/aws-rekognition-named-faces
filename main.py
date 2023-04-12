import boto3
import os

AWS_REGION = "eu-central-1"


def create_dynamodb_table(table_name):
    # Connect to DynamoDB
    dynamodb = boto3.resource("dynamodb", AWS_REGION)

    # Create the table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                "AttributeName": "photo_id",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "photo_id",
                "AttributeType": "S"
            }

        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )

    # Wait until the table is created
    table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
    print(f'DynamoDb table {table_name} has been created !!! ')


def create_collection(collection_name):
    """
    This function creates a collection in AWS Rekognition for storing face images.

    Parameters
    ----------
    collection_name: str
        Name of the collection to create.

    Returns
    -------
    response: dict
        Dictionary containing the status of the operation.
    """

    # Create a client object to call the AWS Rekognition API
    client = boto3.client('rekognition', AWS_REGION)

    try:
        # Create the collection using the collection name
        response = client.create_collection(CollectionId=collection_name)
        # Return the response
        return response

    except Exception as e:
        # Raise exception if there are any errors
        raise e




def upload_to_aws(folder_path, dynamo_db_table_name, collection_name):
    # Connect to AWS Rekognition service
    rekognition = boto3.client("rekognition",AWS_REGION)

    # Connect to AWS DynamoDB
    dynamodb = boto3.resource("dynamodb", AWS_REGION)
    table = dynamodb.Table(dynamo_db_table_name)

    for filename in os.listdir(folder_path):
        # Read image file
        with open(os.path.join(folder_path, filename), "rb") as image:
            response = rekognition.index_faces(
                CollectionId=collection_name,
                Image={
                    "Bytes": image.read()
                }
            )

        # Extract the face ID from the response
        face_id = response["FaceRecords"][0]["Face"]["FaceId"]
        photo_name = filename.split('.')[0]

        # Save the face ID and file name in the DynamoDB table
        table.put_item(
            Item={
                "photo_name": photo_name,
                "photo_id": face_id
            }
        )
        print(f'Photo name {filename} as been uploaded')


def get_photo_name(image_path, collection_id, dynamodb_table_name):
    # Connect to Rekognition
    rekognition = boto3.client("rekognition", AWS_REGION)

    # Read the image
    with open(image_path, "rb") as image_file:
        photo = image_file.read()

    # Search for the face in the collection
    response = rekognition.search_faces_by_image(
        CollectionId=collection_id,
        Image={
            "Bytes": photo
        }
    )

    # Get the face ID from the response
    try:
        face_id = response["FaceMatches"][0]["Face"]["FaceId"]
    except:
        print(f'The image {image_path} hasn\'t identified')
        return

    # Connect to DynamoDB
    dynamodb = boto3.resource("dynamodb", AWS_REGION)

    # Get the table
    table = dynamodb.Table(dynamodb_table_name)

    # Get the photo name for the given face ID
    response = table.get_item(
        Key={
            "photo_id": face_id
        }
    )

    # Return the photo name
    print(f'I See {response["Item"]["photo_name"]} in the photo !!!')
    return response["Item"]["photo_name"]

# 1.  create DyanamoDb table
# create_dynamodb_table('demo_photo_rekognition')
# 2. create a collection
# create_collection('demo-collection')
# 3. upload to images to collection
upload_to_aws('data_set', 'demo_photo_rekognition', 'demo-collection')
# 4. search by image naive
get_photo_name('test/dan_test.jpeg', 'demo-collection', 'demo_photo_rekognition')
# 5 false positive
get_photo_name('test/omer.jpg', 'demo-collection', 'demo_photo_rekognition')
# 6 dan in a group
# get_photo_name('test/dan_in_m2v.jpeg', 'demo-collection', 'demo_photo_rekognition')

# print(upload_to_collection('demo-collection', 'dan.jpeg'))


#
