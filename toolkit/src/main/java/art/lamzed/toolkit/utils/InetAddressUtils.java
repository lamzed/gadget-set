package art.lamzed.toolkit.utils;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressUtils {
    public static String getIpByHostname(String hostname) throws UnknownHostException {
        return InetAddress.getByName("DESKTOP-SERVER2").getHostAddress();
    }
}