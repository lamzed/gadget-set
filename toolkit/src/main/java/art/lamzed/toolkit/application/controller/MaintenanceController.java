package art.lamzed.toolkit.application.controller;

import art.lamzed.toolkit.infrastructure.model.JsonEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/maintenance")
public class MaintenanceController {
    public JsonEntity<?> getActiveThreads() {
        Thread[] activeThreads = new Thread[Thread.activeCount()];
        Thread.enumerate(activeThreads);
        return JsonEntity.ok(activeThreads);
    }
}
