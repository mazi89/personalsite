package com.ledesmahector.somaliuptodate.Web;

import com.ledesmahector.somaliuptodate.Entity.Article;
import com.ledesmahector.somaliuptodate.Exception.ArticleNotFoundException;
import com.ledesmahector.somaliuptodate.Service.ArticleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/parser")
public class Controller {
    private ArticleService articleService;

    @Autowired
    public void setArticleService(ArticleService articleService) {
        this.articleService = articleService;
    }

    @GetMapping("/articles")
    public ResponseEntity<List<Article>> getAllArticles() {
        List<Article> list = articleService.listArticles();
        return new ResponseEntity<List<Article>>(list, HttpStatus.OK);
    }

    @GetMapping("/article/{id}")
    public ResponseEntity<Article> getArticle(@PathVariable("id") long id) {
        try {
            return new ResponseEntity<Article>(articleService.findApplication(id), HttpStatus.OK);
        } catch (ArticleNotFoundException e) {
            throw new ArticleNotFoundException("Application Not Found");
        }
    }


}
