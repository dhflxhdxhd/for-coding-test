import java.io.*;
import java.util.*;

class Inode{
	int row;
	int col;
	int dist;
	public Inode(int row, int col) {
		super();
		this.row = row;
		this.col = col;
	}
	
	public Inode(int row, int col, int dist) {
		super();
		this.row = row;
		this.col = col;
		this.dist = dist;
	} 
}

// 2146. 다리만들기
public class Main {
	

	static boolean[][] visited;
	static int[][] map;
	static int n;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine()); // 지도의 크기 
		
		// 지도 입력
		map = new int[n][n];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 섬 구별하기 
		int cnt = 2;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if(map[i][j] == 1) {
					checkIsland(i,j,cnt);
					cnt++;
				}
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if(map[i][j] >= 2) {
					visited = new boolean[n][n];
					countBridge(i,j);
				}
			}
		}
		
		System.out.println(minDist);
	}	
	
	
	// 상우하좌
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,1,0,-1};
	static int minDist = Integer.MAX_VALUE;
	static void countBridge(int row, int col) {
		Queue<Inode> queue2 = new LinkedList<>();
		queue2.offer(new Inode(row, col, 0));
		int num = map[row][col];
		
		while (!queue2.isEmpty()) {
			Inode inode = queue2.poll();
			visited[inode.row][inode.col] = true;
			
			// 가지치기
			if(inode.dist >=  minDist) {
				return;
			}
						
			for (int d = 0; d < 4; d++) {
				int nr = inode.row + dr[d];
				int nc = inode.col + dc[d];
				
				// 다리 놓기 (경계 안에 있고 && 방문하지 않은 곳이라면)
				if(inArea(nr, nc) && !visited[nr][nc]) {
					visited[nr][nc] = true;
					// 바다라면 다리 1 증가
					if(map[nr][nc] == 0) {
						queue2.offer(new Inode(nr, nc, inode.dist+1));
					// 육지 && 이동 전 대륙의 번호랑 다르면
					}else if(map[nr][nc] != num){
						minDist = Math.min(minDist, inode.dist);
					}
					
				}
			}
		}
	}
	

	static void checkIsland(int row, int col, int cnt) {
		Queue<Inode> queue = new LinkedList<>();
		queue.offer(new Inode(row, col));
		map[row][col] = cnt;
		
		while (!queue.isEmpty()) {
			Inode inode = queue.poll();
			
			for (int d = 0; d < 4; d++) {
				int nr = inode.row + dr[d];
				int nc = inode.col + dc[d];
				
				if(inArea(nr, nc) && map[nr][nc] == 1) {
					map[nr][nc] = cnt;
					queue.offer(new Inode(nr, nc));
				}
			}
		}
	}

	// 경계 안에 있는지 판단하는 메소드
	static boolean inArea(int row, int col) {
		return row >= 0 && row < n && col >= 0 && col < n;
	}
}
