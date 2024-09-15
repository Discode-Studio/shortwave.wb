import java.io.*;
import java.net.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class StreamRedirectServlet extends HttpServlet {

    private static final String SDR_URL = "http://websdr.78dx.ru:8901/?tune=145737.90FM";

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Connexion à l'URL du flux SDR
        URL url = new URL(SDR_URL);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        // Paramétrage de la réponse pour un contenu audio
        resp.setContentType("audio/mpeg");
        resp.setHeader("Content-Disposition", "inline");

        // Lire le flux de l'URL du SDR
        try (InputStream inputStream = connection.getInputStream();
             OutputStream outputStream = resp.getOutputStream()) {

            byte[] buffer = new byte[4096];
            int bytesRead;
            
            // Envoyer le flux audio en continu à la réponse HTTP
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
