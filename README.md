# 🚀 AWS Rekognition Named Faces 📸😎

A fun and easy-to-use solution for identifying people by name using AWS Rekognition and DynamoDB. This repository contains Python code to create and manage face collections, upload and index images, and recognize individuals in photos, providing a seamless integration with AWS services for accurate and efficient face recognition.

## 🛠️ Setup and Installation

1. Make sure you have Python 3.x installed. You can check this by running `python --version` or `python3 --version`.
2. Install the required packages: `pip install boto3`
3. Set up your AWS credentials by following the [official AWS guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
4. Clone this repository to your local machine: `git clone https://github.com/kolodny-coder/aws-rekognition-named-faces.git`

## 🏃‍♂️ How to Use

1. **Create a DynamoDB table** 📚: `create_dynamodb_table('your_table_name')`
2. **Create an AWS Rekognition collection** 🖼️: `create_collection('your_collection_name')`
3. **Upload images to the collection** 📤: `upload_to_aws('your_folder_path', 'your_dynamodb_table_name', 'your_collection_name')`
4. **Search for a person in an image** 🔍😄: `get_photo_name('your_image_path', 'your_collection_name', 'your_dynamodb_table_name')`

Now you can enjoy the power of AWS Rekognition to recognize your friends and have a laugh! 😂🎉

## 🤝 Contributing

Feel free to contribute to this project by submitting issues, bug reports, or feature requests. If you want to add a new feature or fix a bug, just fork the repo, create a new branch, and submit a pull request. We love collaboration! 🤗💻

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- AWS Rekognition and DynamoDB for providing an amazing platform for face recognition. 🌟
- All the cool and funny faces out there that make this project enjoyable. 😜🥳
