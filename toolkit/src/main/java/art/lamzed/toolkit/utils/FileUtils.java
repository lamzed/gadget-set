package art.lamzed.toolkit.utils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class FileUtils {

    public static String USER_DIR = System.getProperty("user.dir");

    public static long G = 1024 * 1024 * 1024;

    public static List<Path> getItems(String path) throws IOException {
        return Files.walk(Paths.get(path)).filter(Files::isRegularFile).collect(Collectors.toList());
    }

    public static boolean isSpaceEnough(String dir) {
        return Paths.get(dir).toFile().getFreeSpace() > 10 * G;
    }
}
