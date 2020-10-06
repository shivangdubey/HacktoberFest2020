class Solution {
    int[] cs;
    Integer[] m;
    Set<Integer> dt;

    public int mincostTickets(int[] dss, int[] cs) {
        this.cs = cs;
        m = new Integer[366];
        dt = new HashSet();
        for (int d: dss) dt.add(d);

        return dp(1);
    }

    public int dp(int i) {
        if (i > 365)
            return 0;
        if (m[i] != null)
            return m[i];

        int ans;
        if (dt.contains(i)) {
            ans = Math.min(dp(i+1) + cs[0],
                               dp(i+7) + cs[1]);
            ans = Math.min(ans, dp(i+30) + cs[2]);
        } else {
            ans = dp(i+1);
        }

        m[i] = ans;
        return ans;
    }
}
