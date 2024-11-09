---
layout: home
---

  <div class="container"
           id="section-about">
    <div class="row">
      <section class="col-md-8">
        {% if site.data.personal.intro.title %}
          <h3 style="font-size:48px">
            {{ site.data.personal.intro.title }}
          </h3>
        {% else %}
          <h3>
            About
          </h3>
        {% endif %}

        <div class="lead">
          {{ site.data.personal.intro.body | markdownify }}
        </div>
        
      </section>
      <section class="col-md-offset-1 col-md-3">
        <style>
        .avatar {
          vertical-align: middle;
          horizontal-align: middle;
          width: 225px;
          height: 225px;
          border-radius: 50%;
        .icon {
          width: 1em;
          height: 1em;
          vertical-align: -0.125em;
        }

        }
        </style>
        <img src="{{ site.baseurl }}{{ site.data.personal.picture }}"
        height="225" hspace="20" alt="Avatar" class="avatar"/>

        <h3>Contact</h3>
        <p>
          {{ site.data.personal.email | replace:'@',' <small>[at]</small> ' | replace:'.',' <small>[dot]</small> ' }}
        </p>
        <p>
          {{ site.data.personal.department }}<br>
          {{ site.data.personal.institution }}<br>
          {{ site.data.personal.mailing_address | replace:'\n','<br>' }}
        </p>
 

        <p>
          <a href="/assets/docs/CV_HReyesNieva.pdf" target="_blank">Curriculum Vitae</a> | <a href="https://scholar.google.com/citations?user=L58_1hAAAAAJ&hl=en" target="_blank">Google Scholar Page</a>
        </p>
        <p>
          Citations: 1156  &nbsp; &nbsp;  h-index: 14
        </p>
        <p>
          {% for profile in site.data.personal.profiles %}
            {% if profile.network == 'LinkedIn' %}
              <i class="fa fa-linkedin-square"></i>
            {% elsif profile.network == 'X/Twitter' %}
              <i class="fa fa-twitter-square"></i>
            {% elsif profile.network == 'Github' %}
              <i class="fa fa-github-square"></i>

            {% endif %}
            <a href="{{ profile.url }}" target="_blank">
              {{ profile.network }}
            </a>
            {% if forloop.last == false %}
              <br>
            {% endif %}
          {% endfor %}
        </p>
      </section>
    </div>
  </div>

  {% if site.data.publications.size > 0 %}
  <div class="container">
    <div class="row">
      <section class="col-md-9">
        <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>  

        <h3>Selected Publications</h3>

        {% for publication in site.data.selected_publications %}
        <p>
        <span data-badge-popover="right" data-badge-type="donut" data-pmid="{{ publication.pmid }}" 
        data-hide-no-mentions="true" class="altmetric-embed" style="float:right" > </span>
            {{ publication.authors }}. 
            <b>
              <a href="{{ publication.pdf }} target='_blank'">
                {{ publication.title }}.
              </a>
            </b>
            
            {% case publication.type %}
              {% when 'conference' %}
                {{ publication.conference }}. {{ publication.year }} {{ publication.month }}. {{ publication.pages }}.

              {% when 'dissertation' %}
                {{ publication.publisher }}

              {% when 'journal' %}
                {{ publication.journal }}. 
                {{ publication.year }}.
                {{ publication.volume }}({{ publication.issue }}):{{ publication.pages }}. PMID: {{ publication.pmid }}.
                <br>
                <b>{{ publication.note}}</b>
        

              {% when 'preprint' %}
          
                {{ publication.server }}.
                {{ publication.year }} {{ publication.month }}. 
                doi: {{ publication.doi }}. 
                <br>
                <b>{{ publication.note}}</b>
                

              {% when 'magazine' %}
                {{ publication.magazine }},
                {{ publication.volume }},
                {{ publication.issue }},
                {{ publication.pages }}
            {% endcase %}

         
          <span class="__dimensions_badge_embed__" data-pmid="{{ publication.pmid }}" data-hide-zero-citations="true"  data-style="large_rectangle"></span></p>
         
        {% endfor %}
        <a href="/publications">--see all publications</a>
        <br>
      </section>
    </div>
  </div>
  {% endif %}

  {% if site.data.projects.size > 0 %}
  <!-- ==================== -->
  <!-- PROJECTS -->
  <!-- ==================== -->
  <section class="container">
    <div class="row">
      <div class="col-md-9">
        <h3>Selected Projects</h3>
      </div>
    </div>

    {% for project in site.data.selected_projects %}
      <div class="row">
        <div class="col-xs-4
                    col-sm-3
                    col-md-3
                    col-lg-2">
          <p>
            <img src="{{ site.baseurl }}{{ project.image }}" 
                 class="img-responsive img-thumbnail"
                 style="width:100%">
          </p>
        </div>
        <div class="col-xs-12
                    col-sm-9
                    col-md-6
                    col-lg-7">
          <p>
            <b>
              {% if project.url %}
                <a href="{{ project.url }}">
                  {{ project.name }}
                </a>
              {% else %}
                {{ project.name }}
              {% endif %}
            </b>
          </p>

          {{ project.description | markdownify }}
        </div>
      </div>
      <br>
    {% endfor %}
    <a href="/projects">--see all projects</a>

  </section>
  {% endif %}

  {% if site.data.presentations.size > 0 %}
  <!-- ==================== -->
  <!-- PRESENTATIONS -->
  <!-- ==================== -->
  <section class="container">
    <div class="row">
      <div class="col-md-9">
        <h3>Selected Presentations</h3>
      </div>
    </div>

    {% for presentation in site.data.selected_presentations %}
      <div class="row">
        <div class="col-md-9">
          <p>
            
              {% if presentation.slides_url %}
                <a href="{{ presentation.slides_url }}">
                  {{ presentation.title }}
                </a>
              {% else %}
                {{ presentation.authors }}. <b><span style="color:#69B3E7;">{{ presentation.title }}</span></b>
              {% endif %}
            
            
            <br>
            <small>{{ presentation.date }}</small> 
            {{ presentation.location }} 
            <br>
            {{ presentation.description }}
          </p>
        </div>
      </div>
    {% endfor %}
    <a href="/presentations">--see all presentations</a>
  </section>
  {% endif %}

  <!-- ==================== -->
  <!-- JAVASCRIPTS -->
  <!-- ==================== -->
  <script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
  <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>  
  <script src="//cdnjs.cloudflare.com/ajax/libs/waypoints/2.0.4/waypoints.min.js"></script>
  <script>
    $(document).ready(function () {
      $('#section-about').waypoint(function (direction) {
        if (direction === 'down') {
          $('body').removeClass('intro-screen');
        } else {
          $('body').addClass('intro-screen');
        }
      });
    });
  </script>