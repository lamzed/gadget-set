package md5demo.src.main.java;

import org.apache.commons.codec.digest.DigestUtils;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class DuplicateKiller {
    private static final String TARGET_PATH = "E:\\tmp";
    private static File targetFolder;
    // fileURL and md5
    private static Map<String, String> allFileAndMD5;
    private static int totalFileDel;
    // delete empty folders
    private static int tmpDelCount;
    private static int totalFolderDel;

    public static void main(String[] args) throws IOException {
        new DuplicateKiller().start();
    }

    private void start() throws IOException {
        init();
        rmDuplicate(targetFolder);
        rmTorrent();
        doDeleteEmptyFolder(targetFolder);
        toBeContinue();
    }

    private void init() throws IOException {
        // hope u can have fun
        System.out.println("############################");
        System.out.println("# welcome2 DuplicateKiller #");
        System.out.println("############################");

        allFileAndMD5 = new HashMap<>();
        targetFolder = new File(TARGET_PATH);
        writer = new BufferedWriter(new FileWriter(targetFolder + File.separator + "console.log"));

        totalFileDel = 0;
        totalFolderDel = 0;
    }

    private void rmDuplicate(File targetFolder) throws IOException {
        File[] files = targetFolder.listFiles();
        assert files != null;
        for (File each : files) {
            if (each.isFile()) {
                String URL = each.getAbsolutePath();
                System.out.println(URL);
                FileInputStream in = new FileInputStream(URL);
                String md5Hex = DigestUtils.md5Hex(in);
                in.close();
                if (!allFileAndMD5.containsKey(md5Hex)) {
                    allFileAndMD5.put(md5Hex, URL);
                } else {
                    int lengthOfURL = URL.split("\\\\").length;
                    String existURL = allFileAndMD5.get(md5Hex);
                    int lengthOfExistURL = existURL.split("\\\\").length;

                    // compare length then rm file while have long path and save short
                    String rmURL = lengthOfExistURL > lengthOfURL ? existURL : URL;
                    String updateURL = lengthOfExistURL < lengthOfURL ? existURL : URL;

                    // when the length is same then dont update the map
                    if (lengthOfExistURL == lengthOfURL) {
                        rmURL = URL;
                    } else {
                        allFileAndMD5.put(md5Hex, updateURL);
                    }

                    boolean delete = new File(rmURL).delete();
                    if (delete) {
                        totalFileDel++;
                    }

                    System.out.println("rm file: [" + delete + "] -> " + rmURL);
                    writer.write("rm file: [" + delete + "] -> " + rmURL);
                    writer.newLine();
                }
            } else {
                rmDuplicate(each);
            }
        }
    }

    private void doDeleteEmptyFolder(File targetFolder) throws IOException {
        System.out.println("############################");
        System.out.println("begin del empty folders...");
        int round = 0;
        do {
            round++;
            System.out.println("round [" + round + "]");
            tmpDelCount = 0;
            deleteEmptyFolder(targetFolder);
            System.out.println("del empty folder [" + tmpDelCount + "]");
        } while (tmpDelCount != 0);
    }

    private void deleteEmptyFolder(File file) throws IOException {
        File[] files = file.listFiles();
        // when files is null means the file above is not folder
        if (files != null) {
            if (files.length != 0) {
                for (File each : files) {
                    deleteEmptyFolder(each);
                }
            } else {
                // cuz file size is 0 then empty folder canb del
                boolean delete = file.delete();
                if (delete) {
                    tmpDelCount++;
                    totalFolderDel++;
                }
                System.out.println("del empty folder: [" + delete + "] -> " + file.getAbsolutePath());
                writer.write("del empty folder: [" + delete + "] -> " + file.getAbsolutePath());
                writer.newLine();
            }
        }
    }

    private void toBeContinue() throws IOException {
        System.out.println("############################");

        System.out.println("total duplicate file del [" + totalFileDel + "]");
        System.out.println("total empty folder del [" + totalFolderDel + "]");
        System.out.println("all output canb check log -> " + DuplicateKiller.targetFolder + File.separator + "console.log");

        writer.newLine();
        writer.write("total duplicate file del: [" + totalFileDel + "]");
        writer.newLine();
        writer.write("total empty folder del: [" + totalFolderDel + "]");
        writer.close();
    }

    private void rmTorrent() throws IOException {
        List<Path> files = Files.walk(Paths.get(TARGET_PATH)).filter(Files::isRegularFile).collect(Collectors.toList());
        for (Path file : files) {
            if (file.getFileName().toString().endsWith(".torrent")) {
                System.out.println("rm .torrent: " + file);
                file.toFile().delete();
            }
        }
    }

    private BufferedWriter writer;
}
