package hello.core;

import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;

@Configuration
// basePackage나 basePackageClasses의 default는 무엇일까?
// 현재 스캔하는 클래스가 있는 패키지가 default임
// 그래서 설정정보 클래스 위치를 프로젝트 최상단에 두는 것을 권장 (스프링부트도!)
// 하위가 모두 자동으로 컴포넌트 스캔의 대상이 되기 때문 + 설정 정보는 프로젝트 정보를 볼 수 있기 때문!
// 그런데... SpringbootApplication 어노테이션에 componentscan이 붙어있어서 부트 쓰면 신경 안써도 됨
// 참고로 컴포넌트 스캔은 Component 어노테이션만 아니라, Service, Controller, Configuration, Repository 다 대상임 왜? -> 해당 어노테이션 코드에 Component가 붙어있음!
// 그런데... 어노테이션은 상속관계라는 것이 없다. 그래서 자바로는 어노테이션이 특정 어노테이션을 들고 있는 것을 인식할 수 없는데... 어노테이션이 관계를 맺는건 Spring 고유 기능임
// 어노테이션에도 다들 역할이 있는데
// @Repository : 데이터 접근 계층으로 인식하고 데이터 계층의 예외를 스프링 예외로 반환해준다.
// @Service : Service는 특별한 처리를 하지 않는다. 대신 개발자들이 비즈니스 로직이 여깄구나!라고 확인 가능
// @Configuration : 스프링 설정정보 인식 및 스프링 빈이 싱글톤을 유지하도록 추가 처리
@ComponentScan(
        basePackages = "hello.core.member",
        basePackageClasses = AutoAppConfig.class,
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)
public class AutoAppConfig {
    // 빈 이름이 중복되면 에러가 남
    // 대신 수동빈과 자동빈이 충돌한다면 수동 빈이 우선권을 가지고 자동 빈을 overriding함
    // 그런데... 정말 잡기 어려운 버그가 만들어짐 왜? 여러 설정이 꼬여버림
    // 그래서 스프링부트에서는 오류가 나도록 바꿔버림 -> 애매한 거보단 오류내는 게 맞다!
    // Test는 통과하지만, Springboot로 Run하면 에러남!
    // 대신 bean-definition-overriding을 설정할 수 있도록!
//    @Bean(name = "memoryMemberRepository")
//    MemberRepository memberRepository() {
//        return new MemoryMemberRepository();
//    }
}
