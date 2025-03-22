const dynamodb = require("aws-sdk/clients/dynamodb");
const docClient = new dynamodb.DocumentClient();
const tableName = process.env.TableName;

const { v4: uuidv4 } = require("uuid");

exports.handler = async (event) => {
  const { name, message } = event;

  const params = {
    TableName: tableName,
    Item: {
      id: uuidv4(),
      name: name,
      message: message,
    },
  };

  const result = await docClient.put(params).promise();

  return result;
};
