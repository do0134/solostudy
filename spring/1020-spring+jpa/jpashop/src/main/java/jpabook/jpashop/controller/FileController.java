package jpabook.jpashop.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.io.File;

@Controller
public class FileController {

    @PostMapping("/files/{fileName}")
    public String createFile(@PathVariable String fileName, @RequestBody String filePath ) {
        File file = new File("C:\\Users\\saffy\\ssafy\\개인공부\\solostudy\\spring\\1020-spring+jpa\\filetest\\"+fileName);
        return "히히";

    }
}
