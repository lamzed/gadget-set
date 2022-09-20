
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DisorderDealer {
    public static void main(String[] args) {
        final List<String> all = new ArrayList<>(54);
        Collections.addAll(all, "🃏JOKER", "🃏joker");

        final List<String> num = new ArrayList<>();
        Collections.addAll(num,
                "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3");
        final List<String> color = new ArrayList<>();
        Collections.addAll(color, "♠", "♥", "♣", "♦");

        for (String n : num) {
            for (String c : color) {
                Collections.addAll(all, c + n);
            }
        }

        Collections.shuffle(all);

        ArrayList<String> player_01 = new ArrayList<>(17);
        ArrayList<String> player_02 = new ArrayList<>(17);
        ArrayList<String> player_03 = new ArrayList<>(17);

        while (all.size() > 3) {
            player_01.add(all.remove(0));
            player_02.add(all.remove(0));
            player_03.add(all.remove(0));
        }

        System.out.println(player_01);
        System.out.println(player_02);
        System.out.println(player_03);
        System.out.println(all);
    }
}
