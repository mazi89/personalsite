package com.ledesmahector.somaliuptodate.Service;

import com.ledesmahector.somaliuptodate.Entity.Article;
import com.ledesmahector.somaliuptodate.Repository.ArticleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ArticleServiceImpl implements ArticleService{

    @Autowired
    private ArticleRepository articleRepository;

    @Override
    public List<Article> listArticles() {
        return (List<Article>) articleRepository.findAll();
    }

    @Override
    public Article findApplication(long id) {
        return null;
    }
}
