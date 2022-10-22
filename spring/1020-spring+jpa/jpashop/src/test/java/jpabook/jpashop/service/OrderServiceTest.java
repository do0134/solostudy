package jpabook.jpashop.service;

import jpabook.jpashop.domain.Address;
import jpabook.jpashop.domain.Item.Book;
import jpabook.jpashop.domain.Item.Item;
import jpabook.jpashop.domain.Member;
import jpabook.jpashop.domain.Order;
import jpabook.jpashop.domain.OrderStatus;
import jpabook.jpashop.domain.exception.NotEnoughStockException;
import jpabook.jpashop.repository.OrderRepository;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;

import static org.junit.jupiter.api.Assertions.*;
@RunWith(SpringRunner.class)
@SpringBootTest
@Transactional
class OrderServiceTest {

    @Autowired
    EntityManager em;
    @Autowired OrderService orderService;
    @Autowired
    OrderRepository orderRepository;

    @Test
    public void 상품주문() throws Exception {
        Member member = new Member();
        member.setName("kim");
        member.setAddress(new Address("서울", "강가", "123123"));
        em.persist(member);

        Item item = new Book();
        item.setName("새책");
        item.setPrice(10000);
        item.setStockQuantity(10);
        em.persist(item);

        int orderCount = 2;
        Long orderId = orderService.order(member.getId(), item.getId(),orderCount);

        Order getOrder = orderRepository.findOne(orderId);

        assertEquals(OrderStatus.ORDER, getOrder.getStatus(), "상품 주문 상태는 ORder" );
        assertEquals(1, getOrder.getOrderItems().size(), "주문 상품 종류 수가 정확해야 한다.");
        assertEquals(10000*orderCount, getOrder.getTotalPrice(), "주문 가격은 수량 * 가격이다");
        assertEquals(8, item.getStockQuantity(), "주문 수량 만큼 재고가 줄어야 한다. ");
    }

    @Test
    public void 주문취소() throws Exception {

        Member member = createMember();
        Book item = createBook("시골", 10000, 19);
        int orderCount = 2;
        Long orderId = orderService.order(member.getId(), item.getId(), orderCount);

        orderService.orderCancel(orderId);

        Order getOrder = orderRepository.findOne(orderId);

        assertEquals(OrderStatus.CANCEL, getOrder.getStatus(), "주문 취소 상태는 캔슬이다");
        assertEquals(19, item.getStockQuantity(), "주문 재고가 돌아와야 된다");

    }

    private Member createMember() {
        Member member = new Member();
        member.setName("회원1");
        member.setAddress(new Address("서울", "강가", "123-123"));
        em.persist(member);
        return member;
    }
    private Book createBook(String name, int price, int stockQuantity) {
        Book book = new Book();
        book.setName(name);
        book.setStockQuantity(stockQuantity);
        book.setPrice(price);
        em.persist(book);
        return book;
    }

    @Test
    public void 상품주문_재고수량초과() throws Exception {

    }

}