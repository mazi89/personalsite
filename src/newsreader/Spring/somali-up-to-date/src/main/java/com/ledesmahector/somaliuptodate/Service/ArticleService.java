package com.ledesmahector.somaliuptodate.Service;

import com.ledesmahector.somaliuptodate.Entity.Article;

import java.util.List;

public interface ArticleService {
    List<Article> listArticles();
    Article findApplication(long id);

}
