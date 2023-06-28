package org.example;

public class PasswordValidator {
    public static final String WRONG_PASSWORD_TEXT = "비밀번호는 최소 8자 이상, 12자 이하여야 한다.";

    public static void validate(String password) {
        int length = password.length();

        if (8 > length || length > 12) {
            throw new IllegalArgumentException(WRONG_PASSWORD_TEXT);
        }
    }
}
