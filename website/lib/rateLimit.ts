const requestTimestamps = new Map<string, number[]>();
const LIMIT = 10;
const WINDOW_MS = 60 * 1000; // 1 minute

export function checkRateLimit(userId: string): boolean {
  const now = Date.now();
  const userRequests = requestTimestamps.get(userId) || [];

  // Remove old requests outside the window
  const validRequests = userRequests.filter((ts) => now - ts < WINDOW_MS);

  if (validRequests.length >= LIMIT) {
    return false;
  }

  validRequests.push(now);
  requestTimestamps.set(userId, validRequests);
  return true;
}
