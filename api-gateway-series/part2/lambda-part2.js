export const handler = async (event) => {
  const { op1, op2 } = event.inputs;
  let result;

  switch (event.operation) {
    case "add":
      result = op1 + op2;
      break;
    case "subtract":
      result = op1 - op2;
      break;
    case "multiply":
      result = op1 * op2;
      break;
    case "divide":
      result = op1 / op2;
      break;
  }

  const response = {
    statusCode: 200,
    body: JSON.stringify(result),
  };
  return response;
};
