package art.lamzed.toolkit.server.utils;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;

public class ExecUtils {
    public static String py(String script) throws IOException, InterruptedException {
        Process process = Runtime.getRuntime().exec("py " + script);
        try (LineNumberReader input = new LineNumberReader(new InputStreamReader(process.getInputStream()))) {
            String result = input.readLine();
            process.waitFor();
            return result;
        }

//        Process process = new ProcessBuilder(py, script).start();
//        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
//        String line;
//        while ((line = reader.readLine()) != null) {
//            System.out.println(line);
//        }
//        return "";
    }
}
