package art.lamzed.toolkit.server.cronjob;

import art.lamzed.toolkit.server.utils.FileUtils;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class PyScripts {
    @Scheduled(cron = "0 0 12 ? * WED")
//    @Scheduled(cron = "0/10 * * * * ?")
    public void audioExtract() {
        System.out.println(FileUtils.USER_DIR);
    }
}
