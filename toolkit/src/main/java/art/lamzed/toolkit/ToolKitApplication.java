package art.lamzed.toolkit;

import art.lamzed.toolkit.application.aspect.LogAspect;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@EnableScheduling
@SpringBootApplication
public class ToolKitApplication {
    private static final Logger log = LoggerFactory.getLogger(LogAspect.class);
    public static void main(String[] args) {
        SpringApplication.run(ToolKitApplication.class, args);
        log.info("Hello world!");
    }
}