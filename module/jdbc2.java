import java.util.*;
import java.sql.*;

public class Exp11{
    public static void main(String args[]) throws Exception{
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost/register","root","root");
            Scanner obj=new Scanner(System.in);
            int n=obj.nextInt();
            for (int i=0;i<n;i++)
            {
                String user=obj.next();
                String pass=obj.next();
      
                PreparedStatement ps=con.prepareStatement("insert into Authentication values(?,?);");
                ps.setString(1,user);
                ps.setString(2, pass);
                ps.executeUpdate();
            }
            Statement stmt = con.createStatement();
            ResultSet rs=stmt.executeQuery("select * from Authentication"); 
            while(rs.next())
            {
                System.out.println(rs.getString(1));
            }
        
        }catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
        
    }}