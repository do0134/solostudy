package jpabook.jpashop.domain;

import lombok.Getter;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.sql.Clob;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Entity
@Getter
public class File {

    @Id @GeneratedValue
    private int Sequence;

    private String fileTitle;

    private String filePath;

    private LocalDateTime createdAt;

    private LocalDateTime updatedAt;

    public void setCreatedAt(LocalDateTime currentTime) {
        createdAt = currentTime;
    }

    public void setUpdatedAt(LocalDateTime currentTime) {
        updatedAt = currentTime;
    }
}
