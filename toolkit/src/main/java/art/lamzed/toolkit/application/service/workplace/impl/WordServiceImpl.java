package art.lamzed.toolkit.application.service.workplace.impl;

import art.lamzed.toolkit.application.service.workplace.WordService;
import org.springframework.stereotype.Service;

@Service
public class WordServiceImpl implements WordService {
    private final static String CN_RE = "[\\u4e00-\\u9fa5]+";

    @Override
    public String wordCount(String str) {
        int words = 0;
        int letters = 0;
        int numbers = 0;

        for (char c : str.toCharArray()) {
            if (Character.toString(c).matches(CN_RE)) {
                words++;
            } else if (Character.isLetter(c)) {
                letters++;
            } else if (Character.isDigit(c)) {
                numbers++;
            }
        }

        return String.format(
                "Total Words %d: Chinese %d Letters %d Numbers %d",
                words + letters + numbers, words, letters, numbers);
    }
}
