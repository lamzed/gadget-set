package art.lamzed.toolkit.infrastructure.model;

public class JsonEntity<T> {
    private boolean success;

    private String message;

    private T data;

    public JsonEntity() {
    }

    public JsonEntity(boolean success) {
        this.success = success;
    }

    public JsonEntity(T data) {
        this.data = data;
    }

    public JsonEntity(boolean success, String message) {
        this.success = success;
        this.message = message;
    }

    public JsonEntity(boolean success, T data) {
        this.success = success;
        this.data = data;
    }

    public JsonEntity(boolean success, String message, T data) {
        this.success = success;
        this.message = message;
        this.data = data;
    }

    public static <T> JsonEntity<?> ok() {
        return new JsonEntity<>(true);
    }

    public static <T> JsonEntity<?>ok(T data) {
        return new JsonEntity<>(true, data);
    }

    public static <T> JsonEntity<?> ok(String message, T data) {
        return new JsonEntity<>(true, message, data);
    }

    public static JsonEntity<?> error(String message) {
        return new JsonEntity<>(false, message);
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }
}