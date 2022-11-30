export const handler = async (event) => {
  // TODO implement

  const response = {
    statusCode: 200,
    body: `Hellow from ${event["queryStringParameters"]["name"]} and ${event["pathParameters"]["name"]}`,
  };

  return response;
};
