<%@ page import = "java.sql.*" %>
<%
String username = request.getParameter("username");
String password = request.getParameter("password");
String email = request.getParameter("email");



try {
    Class.forName("com.mysql.cj.jdbc.Driver");
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:/register", "root", "root");
    PreparedStatement ps = conn.prepareStatement("insert into signup(username, password,email) values (?, ?, ?)");
    ps.setString(1, username);
    ps.setString(2, password);
    ps.setString(3, email);
    int x = ps.executeUpdate();
    if (x > 0) {
                response.sendRedirect("inner.html");
    }
    else {
        
                out.print("<html><body>");
                out.println("<script>");
                out.println("Registration failed");
                out.print("window.location.href = 'signup.html';");
                out.println("</script>");
                out.println("</body></html>");
    }

}
catch(Exception e) {
    out.println(e);
}


%>
