public class Exp11 {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); 
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/register", "root", "root");
            Statement stmt = con.createStatement();
//            String query = "CREATE TABLE Authentication (username VARCHAR(30), password VARCHAR(30))";
//            stmt.executeUpdate(query);
                //System.out.println("Table 'Authentication' created successfully!");
//            String query1 = "insert into Authentication values ('sriram','4016')";
//            stmt.executeUpdate(query1);
                ResultSet rs=stmt.executeQuery("select * from Authentication where password='4009'"); 
                while(rs.next())
                {
                    if(rs.getString(1)==null)
                        System.out.println("Not prsent");
                    else {
                        System.out.println(rs.getString(1));
                    }
                }
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}