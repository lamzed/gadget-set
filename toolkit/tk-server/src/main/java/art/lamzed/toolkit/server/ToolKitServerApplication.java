package art.lamzed.toolkit.server;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan
@SpringBootApplication
public class ToolKitServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ToolKitServerApplication.class, args);
    }
}