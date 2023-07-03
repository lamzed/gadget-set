package art.lamzed.toolkit.utils;

public class TextUtils {
    private final static String COUNTER_RE = "[\\u4e00-\\u9fa5aA-Za-z0-9]";
    private final static String CN_RE = "[\\u4e00-\\u9fa5]+";

    public static String textCounter(String input) {
        int words = 0;
        int letters = 0;
        int numbers = 0;

        for (char c : input.toCharArray()) {
            if (Character.toString(c).matches(CN_RE)) {
                words++;
            } else if (Character.isLetter(c)) {
                letters++;
            } else if (Character.isDigit(c)) {
                numbers++;
            }
        }
        return String.format("Total Words %d: Chinese %d Letters %d Numbers %d", words + letters + numbers, words, letters, numbers);
    }

    public static void main(String[] args) {
        System.out.println(textCounter("这是一个句子aaaAAAda31487"));
    }
}
