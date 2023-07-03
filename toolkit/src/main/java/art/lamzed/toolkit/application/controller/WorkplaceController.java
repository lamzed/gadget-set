package art.lamzed.toolkit.application.controller;

import art.lamzed.toolkit.application.service.workplace.WordService;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@RequestMapping("/workplace")
public class WorkplaceController {
    @Resource
    WordService wordService;

    @PostMapping("/wordCount")
    public String wordCount(@RequestBody String str) {
        return wordService.wordCount(str);
    }
}
