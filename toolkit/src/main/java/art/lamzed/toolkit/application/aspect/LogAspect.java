package art.lamzed.toolkit.application.aspect;

import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LogAspect {
    private static final Logger log = LoggerFactory.getLogger(LogAspect.class);

    @Pointcut("execution(public * art.lamzed.toolkit.application.controller..*.*(..))")
    public void logPointCut() {
    }

    @Around("logPointCut()")
    public void doAround() {
    }
}
