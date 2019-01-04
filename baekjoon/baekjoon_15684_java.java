import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

import java.util.*;


public class Main{

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N, M, H;
        N = sc.nextInt();
        M = sc.nextInt();
        H = sc.nextInt();
    
        int[][] ladder = new int[N][H];
        
        for(int i = 0; i < M; i++){
            int a,b;
            a = sc.nextInt()-1;
            b = sc.nextInt()-1;
            ladder[b][a] = 1;
            ladder[b+1][a] = -1;
        }
        
        int result = solution(N, H, ladder);
        System.out.println(result);

    }
    
    
    private static boolean comb_ladders(int N, int H, int[][] ladder, int more_line, int start_idx){
        if(more_line == 0){
            return simulation(N,H,ladder);
        }
        
        for (int idx=start_idx; idx<(N-1)*H; idx++){
            int a = idx / (N-1);
            int b = idx % (N-1);
            if(ladder[b][a] != 0 || ladder[b+1][a] != 0){
                continue;
            }
            else{
                //add line
                ladder[b][a] = 1;
                ladder[b+1][a] = -1;
                
                if(comb_ladders(N, H, ladder, more_line-1, idx+1)){
                    return true;
                }
                //remove line => backtracking
                ladder[b][a] = 0;
                ladder[b+1][a] = 0;
            }
        }
        
        return false;
        
    }
    
    
    private static int solution(int N, int H, int[][] ladder){
        //System.out.println(N + "" + H + "" + Arrays.deepToString(ladder));

        //System.out.println(Arrays.deepToString(ladders.get(0).getL()));
        
        for (int i=0; i<4; i++){
            if (comb_ladders(N, H, ladder, i, 0)){
                return i;
            }
        }
                
        return -1;
        
    }
    
    private static boolean simulation(int N, int H, int[][] ladder){
        int count = 0;
        for (int[] col : ladder){
            for (int i=0; i<col.length; i++){
                if(col[i] == 1){
                    count++;
                }
            }
        }
        if(count%2 != 0){
            return false;
        }
        
        for(int c=0; c<N; c++){
            //System.out.println(simul_single_col(c,0,ladder));
            if(c != simul_single_col(c,H,ladder)){
                return false;
            }
        }
        return true;
    }
    
        
    private static int simul_single_col(int curr_col, int H, int[][] ladder){
        for(int row=0; row<H; row++){
            if(ladder[curr_col][row] != 0){
                curr_col = curr_col + ladder[curr_col][row];
            }
        }
        return curr_col;
    }
    
}