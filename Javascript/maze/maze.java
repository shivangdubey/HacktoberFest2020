import java.awt.Point;
import java.util.LinkedList;
import java.util.Queue;


public class Progress5 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//transformasikan Maze2D menjadi array 2D
		int[][]maze={{
				-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},{
				-1,0,0,0,-1,-1,0,-1,-1,0,-1},{
				-1,0,-1,0,-1,-1,0,0,0,0,-1},{
				-1,0,0,0,0,-1,0,-1,-1,0,-1},{
				-1,-2,0,-1,0,-1,0,-1,-1,0,-1},{
				-1,-1,0,-1,0,0,0,-1,-1,0,-1},{
				-1,-1,0,-1,-1,-1,0,-1,-1,0,-3},{
				-1,0,0,0,0,0,0,-1,-1,0,-1},{
				-1,0,-1,-1,0,-1,0,-1,-1,0,-1},{
				-1,0,0,0,0,-1,0,0,0,0,-1},{
				-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}	
		};
		
		System.out.println("Initial Maze");
		tampilkanArray(maze);
		
		boolean selesai	= false;
		LinkedList<Point> queue=new LinkedList<Point>();
		
		Point start	= new Point(4,1);
		
		queue.offer(start);
		int step = 0;
		
		//MELAKUKAN LANGKAH BFS
		while(!selesai&&!queue.isEmpty()){
			Point c	= queue.poll();

			if(maze[c.x][c.y]==-2){
				step=0;
			}else{
				step	= maze[c.x][c.y];
			}			
			
			//MOVE-UP
			int x	= c.x-1;
			int y	= c.y;
			if(x>=0&&maze[x][y]==0){
				maze[x][y]=1+step;
				Point newPoint	= new Point(x,y);
				queue.offer(newPoint);							
			}else if(maze[x][y]==-3){
				selesai=true;
				System.out.println("FINISH");
				break;
			}
			
			//MOVE-RIGHT
			x	= c.x;
			y	= c.y+1;
			if(y<maze[x].length&&maze[x][y]==0){
				maze[x][y]=1+step;
				Point newPoint	= new Point(x,y);
				queue.offer(newPoint);							
			}else if(maze[x][y]==-3){
				selesai=true;
				System.out.println("FINISH");
				break;
			}
			
			//MOVE-DOWN
			x	= c.x+1;
			y	= c.y;
			if(x<maze.length&&maze[x][y]==0){
				maze[x][y]=1+step;
				Point newPoint	= new Point(x,y);
				queue.offer(newPoint);							
			}else if(maze[x][y]==-3){
				selesai=true;
				System.out.println("FINISH");
				break;
			}
			
			//MOVE-RIGHT
			x	= c.x;
			y	= c.y-1;
			if(y>=0&&maze[x][y]==0){
				maze[x][y]=1+step;
				Point newPoint	= new Point(x,y);
				queue.offer(newPoint);							
			}else if(maze[x][y]==-3){
				selesai=true;
				System.out.println("FINISH");
				break;
			}
		}	

		//SELESAI		
		System.out.println("Jumlah Langkah :"+(1+step));
		tampilkanArray(maze);

	}
	
	public static void tampilkanArray(int[][]array){
		for(int i=0;i<array.length;i++){
			for(int j=0;j<array[i].length;j++){
				System.out.print(array[i][j]+",");
			}
			System.out.println();
		}
	}

}
