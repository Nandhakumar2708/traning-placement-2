class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] ugly = new int[n];
        ugly[0] = 1;

        int k = primes.length;
        int[] idx = new int[k];
        long[] val = new long[k]; // use long for intermediate values

        Arrays.fill(val, 1);

        for (int i = 1; i < n; i++) {
            long next = Long.MAX_VALUE;
            for (int j = 0; j < k; j++) {
                val[j] = (long) primes[j] * ugly[idx[j]];
                next = Math.min(next, val[j]);
            }
            ugly[i] = (int) next; // safe cast because result fits in int

            for (int j = 0; j < k; j++) {
                if (val[j] == next) {
                    idx[j]++;
                }
            }
        }

        return ugly[n - 1];

    }
}
