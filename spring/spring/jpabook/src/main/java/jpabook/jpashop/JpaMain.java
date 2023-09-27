package jpabook.jpashop;

import javax.persistence.*;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory etf = Persistence.createEntityManagerFactory("hello");

        EntityManager em = etf.createEntityManager();
        EntityTransaction tx = em.getTransaction();

        tx.begin();

        try {
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }

        etf.close();

    }

}
