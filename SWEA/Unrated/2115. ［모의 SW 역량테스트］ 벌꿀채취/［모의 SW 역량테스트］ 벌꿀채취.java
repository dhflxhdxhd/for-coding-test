import java.io.*;
import java.util.*;

public class Solution {

	static int[][] beehive, profits;
	static int n, m, c, maxProfit = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();

		int t = Integer.parseInt(br.readLine());

		for (int test = 1; test <= t; test++) {
			sb.append("#").append(test+" ");
			
			
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken()); // 벌통들의 크기
			m = Integer.parseInt(st.nextToken()); // 선택할 수 있는 벌통의 개수
			c = Integer.parseInt(st.nextToken()); // 꿀을 채취할 수 있는 최대 양

			beehive = new int[n][n];
			profits = new int[n][n];

			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					beehive[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			// 1. 각 셀에서 얻을 수 있는 최대 수익
			makeProfit();
			
//			printProfits();
			
			// 2. 두 일꾼이 채취할 공간 고르기
			getHoney();
			
			sb.append(maxProfit).append("\n");
		}
		
		System.out.println(sb.toString());
		
	}
	
	static void printProfits() {
		for (int i = 0; i < n; i++) {
			System.out.println(Arrays.toString(profits[i]));
		}
	}
	
	static void getHoney() {
		maxProfit = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= n-m; j++) {
				pickSpace(i,j+m,1, profits[i][j]);
			}
		}
	}
	

	static void pickSpace(int r, int c, int person, int mp) {
		if(person == 2) { // 일꾼 두 명 다 뽑았다면
			maxProfit = Math.max(maxProfit, mp);
			return;
		}
		
		for (int i = r; i < n ; i++) {
			for (int j = c; j <= n-m; j++) {
				pickSpace(i, j+m, person+1, mp + profits[i][j]);
			}
			c = 0;
		}
	}

	static void makeProfit() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= n-m; j++) {
				calProfit(i, j, 0, 0, 0);
			}
		}
	}

	static void calProfit(int row, int col, int cnt, int sum, int total) {
		if (sum > c) {
			return;
		}

		if (cnt == m) {
			profits[row][col-m] = Math.max(profits[row][col - m], total);
			return;
		}

		// 현재공간 꿀 얻기
		calProfit(row, col + 1, cnt + 1, sum + beehive[row][col], total + beehive[row][col] * beehive[row][col]);
		// 현재 공간에서 꿀 X
		calProfit(row, col + 1, cnt + 1, sum, total);
	}
}
