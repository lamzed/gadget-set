package art.lamzed.toolkit.infrastructure.model;

public class JsonEntity<T> {
    private boolean success;

    private String message;

    private T data;

    public JsonEntity() {
    }

    public JsonEntity(boolean success, String message, T data) {
        this.success = success;
        this.message = message;
        this.data = data;
    }
}
