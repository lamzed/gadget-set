package art.lamzed.toolkit.server.service;

import art.lamzed.toolkit.server.utils.ExecUtils;
import art.lamzed.toolkit.server.utils.FileUtils;
import org.springframework.stereotype.Service;

import java.io.IOException;

@Service
public class CmdService {
    public String extractor(String path) {
        try {
//            return ExecUtils.py("E:\\repositories\\toolkit\\src\\main\\resources\\scripts\\hello.py");
            System.out.println(FileUtils.USER_DIR + "audio_extractor\\extractor.py");
            return ExecUtils.py("E:\\repositories\\toolkit\\src\\main\\resources\\scripts\\audio_extractor\\extractor.py");
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
