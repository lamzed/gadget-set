package art.lamzed.toolkit.application.handler;

import art.lamzed.toolkit.infrastructure.model.JsonEntity;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

@ControllerAdvice
@ResponseBody
public class GlobalExceptionHandler {
    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(Exception.class)
    public JsonEntity<?> exceptionHandler() {
        return JsonEntity.ok();
    }

    private Throwable getInnerException(Throwable cause) {
        if (cause.getCause() == null) {
            return cause;
        }
        return getInnerException(cause.getCause());
    }
}
