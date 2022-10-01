package art.lamzed.toolkit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class ToolKitApplication {
    public static void main(String[] args) {
        SpringApplication.run(ToolKitApplication.class, args);
    }
}