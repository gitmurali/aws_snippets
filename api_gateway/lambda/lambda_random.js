exports.handler = async (event) => {
  const quotes = [
    "Stay Hungry. Stay Foolish.",
    "Good Artists Copy, Great Artists Steal.",
    "Argue with idiots, and you become an idiot.",
    "Be yourself; everyone else is already taken.",
    "Simplicity is the ultimate sophistication.",
  ];

  return quotes[Math.floor(Math.random() * 5)];
};
