package art.lamzed.toolkit.application.controller;

import art.lamzed.toolkit.application.service.workplace.WordsService;
import art.lamzed.toolkit.infrastructure.model.JsonEntity;
import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/workplace")
public class WorkplaceController {
    @Resource
    WordsService wordsService;

    @PostMapping("/wordsCount")
    public JsonEntity<?> wordsCount(@RequestBody String str) {
        return JsonEntity.ok(wordsService.wordsCount(str));
    }
}
