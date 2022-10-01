package src.version1_3;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Breath {
    // input
    private static File file;
    private static String path;
    private static String[] suffixs;
    // temp
    private static ArrayList<File> all_target_file = new ArrayList<>();
    // output
    private static HashSet<String> all_file_type = new HashSet<>();
    private static HashMap<String, String> same_name_file = new HashMap<>();
    private static HashMap<String, String> same_size_file = new HashMap<>();

    public static void main(String[] args) throws IOException {
        welcome();
        search();
        result();
    }

    // for all file type.
    // and all the target file according the input String[] suffixs
    private static void forAllTypeAndAllTarget(File dir) {
        File[] files = dir.listFiles();
        assert files != null;
        for (File each_file : files) {
            if (each_file.isFile()) {
                // for file suffix also the file type
                String[] tmp = each_file.getName().split("\\.");
                // if tmp.length > 1 then save the file's name to a new arraylist.
                // example: xxx.png is ok; and xxx not
                if (tmp.length > 1) {
                    // get suffix
                    all_file_type.add(tmp[tmp.length - 1]);
                }

                // for all the file that you want
                // end with the suffixs you set
                for (String suffix : suffixs) {
                    if (each_file.getName().endsWith(suffix)) {
                        all_target_file.add(each_file);
                    }
                }

            } else if (each_file.isDirectory()) {
                forAllTypeAndAllTarget(each_file);
            }
        }
    }

    private static void result() {
        System.out.println();
        System.out.println("all file type: ");
        System.out.println(all_file_type);
        System.out.println();
        // System.out.println(all_target_file);
        // System.out.println(same_name_file);

        System.out.println("all same name file: ");
        Set<Map.Entry<String, String>> get = same_name_file.entrySet();
        for (Map.Entry<String, String> e : get) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }
        System.out.println();

        System.out.println("all same size file: ");

        Set<Map.Entry<String, String>> get_ = same_size_file.entrySet();
        for (Map.Entry<String, String> e : get_) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }
    }

    private static void initialize() throws IOException {
        Properties config = new Properties();
        config.load(new FileReader("duplicate_killer\\src\\version1_3\\info.properties"));
        if (!(config.size() == 1)) {
            System.out.println("makesure only one key one value");
        }
        Set<String> names = config.stringPropertyNames();
        for (String name : names) {
            path = name;
            String value = config.getProperty(name);
            suffixs = value.split(",( )*");
        }
        file = new File(path);
    }

    private static void welcome() throws IOException {
        System.out.println("############################");
        System.out.println("# welcome2 DuplicateKiller #");
        System.out.println("############################");
        // System.out.println("# plz enter your path: ");
        initialize();
    }

    private static void search() {
        System.out.println("running plz wait...");
        forAllTypeAndAllTarget(file);
        killRepeatAndSameSize();
    }

    // duplicate killer
    private static void killRepeatAndSameSize() {
        // for all file'name that are same, put them as key in map
        // and the value are their path
        for (int i = 0; i < all_target_file.size(); i++) {
            for (int j = i + 1; j < all_target_file.size(); j++) {
                File fileI = all_target_file.get(i);
                File fileJ = all_target_file.get(j);
                String tmp_path = fileI.getAbsolutePath() + ", " + fileJ.getAbsolutePath();

                // if two file name are same and path are not
                if (fileI.getName().equals(fileJ.getName())
                        && !fileI.getAbsolutePath().equals(fileJ.getAbsolutePath())) {
                    // the file's name first put in map
                    if (!same_name_file.containsKey(fileI.getName())) {
                        same_name_file.put(fileI.getName(), tmp_path);
                    } else {
                        // if file path already exist, then invoke "+" method of String
                        tmp_path = ", " + fileJ.getAbsolutePath();
                        String exist_path = fileI.getAbsolutePath();
                        same_name_file.put(fileI.getName(), exist_path + tmp_path);
                    }
                }

                // get all file that size are same while path not
                if (fileI.length() == fileJ.length()
                        && !fileI.getAbsolutePath().equals(fileJ.getAbsolutePath())) {
                    // if the kay first put in map
                    if (!same_size_file.containsKey(fileI.getName())) {
                        same_size_file.put(fileI.getName(), tmp_path);
                    } else {
                        tmp_path = ", " + fileJ.getAbsolutePath();
                        String exist_path = fileI.getAbsolutePath();
                        same_size_file.put(fileI.getName(), exist_path + tmp_path);
                    }
                }
                // System.out.println("?"+fileI+"::"+fileJ);
            }
        }
    }
}
