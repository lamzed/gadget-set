package art.lamzed.toolkit.server.controller;

import art.lamzed.toolkit.server.model.vo.ScriptVO;
import art.lamzed.toolkit.server.service.CmdService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.Optional;

@Controller
public class CmdController {

    @Resource
    private CmdService cmdService;

    @GetMapping("/exe")
    public String index(Model model) {
        ArrayList<ScriptVO> scriptVOS = new ArrayList<>();
        scriptVOS.add(new ScriptVO("111", "pwd"));
        scriptVOS.add(new ScriptVO("121", "pwd"));
        scriptVOS.add(new ScriptVO("131", "pwd"));
        scriptVOS.add(new ScriptVO("141", "pwd"));
        scriptVOS.add(new ScriptVO("181", "pwd"));
        model.addAttribute("scripts", scriptVOS);
        return "commands";
    }

    @PostMapping("/reword")
    @ResponseBody
    public String demo(String path) {
        if ("".equals(path)) {
            System.out.println("null");
        }
        System.out.println("..." + Optional.of(path).orElse("where"));
        System.out.println(": " + path);
        return "ok";
    }

    @PostMapping("/extract")
    @ResponseBody
    public String extractor(String path) {
        if ("".equals(path)) {
            System.out.println("null");
        }
        return cmdService.extractor(path);
    }
}
