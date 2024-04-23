package jpabook.jpashop.controller;

import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;


@RestController
@Slf4j
public class HomeController {

    @RequestMapping("/home")
    public String home() {
        log.info("home controller");
        return "home";
    }
    public static void showFilesInDIr (String path) {
        File file = new File(path);
        File files[] = file.listFiles();
        String names[] = file.list();

        for (int i = 0; i < files.length; i++) {
            File dir = files[i];
            String name = names[i];
            if (file.isDirectory()) {
                showFilesInDIr(dir.getPath());

            } else {
                System.out.println("file: " + file);
                System.out.println(name);
            }
        }
    }
    @GetMapping("/")
    public ResponseEntity<String> pjtRead() {
        String baseUrl = "C:\\Users\\multicampus\\Desktop\\test";
        showFilesInDIr(baseUrl);

        return new ResponseEntity<>("1", HttpStatus.ACCEPTED);

    }
}
