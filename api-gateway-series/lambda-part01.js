// How to pass path params and query strings

export const handler = async (event) => {
  const response = {
    statusCode: 200,
    body: `Good ${event["queryStringParameters"]["greeting"]},  nice to meet you ${event["pathParameters"]["name"]}!!`,
  };

  return response;
};
