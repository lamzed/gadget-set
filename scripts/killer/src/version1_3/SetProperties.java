package src.version1_3;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;

// example for seting properties
// or you can set the key and value in [info.properties] directly
public class SetProperties {
    public static void main(String[] args) throws IOException {
        // path + suffix
        Properties config = new Properties();
        config.setProperty("D:\\example\\example",".java,    .python,.png, .mp3"); // regex split " *"
        config.store(new FileWriter("duplicate_killer\\src\\version1_3\\info.properties"),
                "the key&value are path + suffix");
    }
}
